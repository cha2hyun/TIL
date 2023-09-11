import { Query, Resolver } from '@nestjs/graphql';

@Resolver()
export class UserResolver {
  @Query(() => String)
  sayPing() {
    return 'pong';
  }

  @Query(() => String)
  whatUser() {
    return 'its me';
  }
}
